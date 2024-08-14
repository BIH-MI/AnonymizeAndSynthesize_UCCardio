/**
 * Use Case Cardiology HiGHmed Data Anonymisation
 * Copyright (C) 2023 - Berlin Institute of Health
 * <p>
 * Use of this software is govered by the Business Source License included in the LICENSE.md file.
 * Change Date: 14.08.2028, Change License: Academic Free License v3.0
 * On the date above, in accordance with the Business Source License, use of this software will be governed by the
 * open source license AFL v3.0 or as specified in the LICENSE.md file.
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.bihmi.usecase_cardiology;

import org.deidentifier.arx.Data;
import org.deidentifier.arx.DataHandle;
import org.deidentifier.arx.DataHandleOutput;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Utility class, code was adapted from: <a href="https://github.com/BIH-MI/leoss-puf">LEOSS Repository</a>
 *
 * @author Fabian Prasser
 */
public class Util {

    /**
     * Extract data
     * @param handle
     * @return
     */
    public static Data getData(DataHandle handle) {

        // Prepare
        Iterator<String[]> iter = handle.iterator();
        List<String[]> rows = new ArrayList<>();
        rows.add(iter.next());
        int rowNumber = 0;
        
        // Convert
        while (iter.hasNext()) {
            String[] row = iter.next();
            if (!(handle instanceof DataHandleOutput) || !handle.isOutlier(rowNumber)) {
                rows.add(row);
            }
            rowNumber++;
        }
        
        // Done
        return Data.create(rows);
    }
    
}

